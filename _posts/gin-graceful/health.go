package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

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
