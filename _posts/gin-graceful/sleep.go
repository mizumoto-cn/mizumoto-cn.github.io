package main

import (
	"fmt"
	"net/http"
	"strconv"
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
