package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

func jp_wk(wd time.Weekday) string {
	switch wd.String() {
	case "Sunday":
		return "日曜日"
	case "Monday":
		return "月曜日"
	case "Tuesday":
		return "火曜日"
	case "Wednesday":
		return "水曜日"
	case "Thursday":
		return "木曜日"
	case "Friday":
		return "金曜日"
	case "Saturday":
		return "土曜日"
	}
	return ""
}

func jp_mn(wd time.Month) string {
	switch wd.String() {
	case "January":
		return "一月"
	case "February":
		return "ニ月"
	case "March":
		return "三月"
	case "April":
		return "四月"
	case "May":
		return "五月"
	case "June":
		return "六月"
	case "July":
		return "七月"
	case "August":
		return "八月"
	case "September":
		return "九月"
	case "October":
		return "十月"
	case "November":
		return "十一月"
	case "December":
		return "十二月"
	}
	return ""
}

func largeFormat(mn time.Month, wd time.Weekday, d, h, m int) {
	fmt.Printf("%s %s %d日, %d時%d分", jp_mn(mn), jp_wk(wd), d, h, m)
}

func shortFormat(wd time.Weekday, d, h, m int) {
	fmt.Printf("%s %d日, %d時%d分", jp_wk(wd), d, h, m)
}

func main() {
	currentTime := time.Now()
	_, mn, d := currentTime.Date()
	wd := currentTime.Weekday()
	h := currentTime.Hour()
	m := currentTime.Minute()

	switch strings.ToLower(os.Args[1]) {
	case "short":
		shortFormat(wd, d, h, m)
	case "large":
		largeFormat(mn, wd, d, h, m)
	default:
		os.Exit(1)
	}
}
