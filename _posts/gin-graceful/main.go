package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/signal"
	"strconv"
	"syscall"
	"time"

	"github.com/gin-gonic/gin"
)

// 模拟慢请求
func sleep(ctx *gin.Context) {
	t := ctx.Query("t")
	s, err := strconv.Atoi(t)
	if err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"msg": "参数错误: " + t})
		return
	}

	time.Sleep(time.Duration(s) * time.Second)
	ctx.JSON(http.StatusOK, gin.H{"msg": fmt.Sprintf("sleep %d s", s)})
}

const (
	stateHealth   = "health"
	stateUnHealth = "unhealth"
)

var state = stateHealth

func health(ctx *gin.Context) {
	status := http.StatusOK
	if state == stateUnHealth {
		status = http.StatusServiceUnavailable
	}
	ctx.JSON(status, gin.H{"data": state})
}

func main() {
	e := gin.Default()
	e.GET("/health", health)
	e.GET("/sleep", sleep)

	server := &http.Server{
		Addr:    ":8080",
		Handler: e,
	}

	go func() {
		if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("server run err: %+v", err)
		}
	}()

	// 用于捕获退出信号
	quit := make(chan os.Signal)

	// kill (no param) default send syscall.SIGTERM
	// kill -2 is syscall.SIGINT
	// kill -9 is syscall.SIGKILL but can't be catch, so don't need add it
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit
	log.Println("Shutting down server...")

	// 捕获到退出信号之后将健康检查状态设置为 unhealth
	state = stateUnHealth
	log.Println("Shutting down state: ", state)

	// 设置超时时间，两个心跳周期，假设一次心跳 3s
	ctx, cancel := context.WithTimeout(context.Background(), 6*time.Second)
	defer cancel()

	// Shutdown 接口，如果没有新的连接了就会释放，传入超时 context
	// 调用这个接口会关闭服务，但是不会中断活动连接
	// 首先会将端口监听移除
	// 然后会关闭所有的空闲连接
	// 然后等待活动的连接变为空闲后关闭
	// 如果等待时间超过了传入的 context 的超时时间，就会强制退出
	// 调用这个接口 server 监听端口会返回 ErrServerClosed 错误
	// 注意，这个接口不会关闭和等待websocket这种被劫持的链接，如果做一些处理。可以使用 RegisterOnShutdown 注册一些清理的方法
	if err := server.Shutdown(ctx); err != nil {
		log.Fatal("Server forced to shutdown:", err)
	}

	log.Println("Server exiting")
}
