package main

import (
    "fmt"
)

func main(){
    var multi [9][9]string
    for j := 1; j < 9; j++{
        for  i := 1; i < 9; i++{
            n1 := i+1
            n2 := j+1
            // 防止重复
            // 随时保持 n1 > n2
            if n1 < n2 {
                continue
            }
            fmt.Sprintf("%dx%d=%d", n2, n1, n2*n1)
        }
    }

    // print 
    for  _, v1 := range multi {
        for  _, v2 := v1 {
            // 每个之间8位宽度
            fmt.Printf("%-8s",v2)
        }
        fmt.Println()
    }
}

