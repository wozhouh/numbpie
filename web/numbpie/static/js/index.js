jQuery(document).ready(function ($) {
    $(".big-box .item").height((document.body.clientHeight) + "px")


    var jssor_1_SlideshowTransitions = [
        {
            $Duration: 1200,
            x: 0.3,
            $During: {$Left: [0.3, 0.7]},
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: -0.3,
            $SlideOut: true,
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: -0.3,
            $During: {$Left: [0.3, 0.7]},
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: 0.3,
            $SlideOut: true,
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: 0.3,
            $During: {$Top: [0.3, 0.7]},
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: -0.3,
            $SlideOut: true,
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: -0.3,
            $During: {$Top: [0.3, 0.7]},
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: 0.3,
            $SlideOut: true,
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: 0.3,
            $Cols: 2,
            $During: {$Left: [0.3, 0.7]},
            $ChessMode: {$Column: 3},
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: 0.3,
            $Cols: 2,
            $SlideOut: true,
            $ChessMode: {$Column: 3},
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: 0.3,
            $Rows: 2,
            $During: {$Top: [0.3, 0.7]},
            $ChessMode: {$Row: 12},
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: 0.3,
            $Rows: 2,
            $SlideOut: true,
            $ChessMode: {$Row: 12},
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: 0.3,
            $Cols: 2,
            $During: {$Top: [0.3, 0.7]},
            $ChessMode: {$Column: 12},
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            y: -0.3,
            $Cols: 2,
            $SlideOut: true,
            $ChessMode: {$Column: 12},
            $Easing: {$Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: 0.3,
            $Rows: 2,
            $During: {$Left: [0.3, 0.7]},
            $ChessMode: {$Row: 3},
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: -0.3,
            $Rows: 2,
            $SlideOut: true,
            $ChessMode: {$Row: 3},
            $Easing: {$Left: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: 0.3,
            y: 0.3,
            $Cols: 2,
            $Rows: 2,
            $During: {$Left: [0.3, 0.7], $Top: [0.3, 0.7]},
            $ChessMode: {$Column: 3, $Row: 12},
            $Easing: {$Left: $Jease$.$InCubic, $Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            x: 0.3,
            y: 0.3,
            $Cols: 2,
            $Rows: 2,
            $During: {$Left: [0.3, 0.7], $Top: [0.3, 0.7]},
            $SlideOut: true,
            $ChessMode: {$Column: 3, $Row: 12},
            $Easing: {$Left: $Jease$.$InCubic, $Top: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            $Delay: 20,
            $Clip: 3,
            $Assembly: 260,
            $Easing: {$Clip: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            $Delay: 20,
            $Clip: 3,
            $SlideOut: true,
            $Assembly: 260,
            $Easing: {$Clip: $Jease$.$OutCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            $Delay: 20,
            $Clip: 12,
            $Assembly: 260,
            $Easing: {$Clip: $Jease$.$InCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        },
        {
            $Duration: 1200,
            $Delay: 20,
            $Clip: 12,
            $SlideOut: true,
            $Assembly: 260,
            $Easing: {$Clip: $Jease$.$OutCubic, $Opacity: $Jease$.$Linear},
            $Opacity: 2
        }
    ];
    var jssor_1_slider = new $JssorSlider$("scroll_tree", {
        $AutoPlay: false,
        $SlideshowOptions: {
            $Class: $JssorSlideshowRunner$,
            $Transitions: jssor_1_SlideshowTransitions,
            $TransitionsOrder: 1
        },
        $ArrowNavigatorOptions: {
            $Class: $JssorArrowNavigator$
        },
        $ThumbnailNavigatorOptions: {
            $Class: $JssorThumbnailNavigator$,
            $Cols: 10,
            $SpacingX: 8,
            $SpacingY: 8,
            $Align: 360
        }
    });


    $.ajax({
        type: 'GET',
        url: 'https://www.tianqiapi.com/api/',
        data: 'version=v1&style=1001&city=',
        dataType: 'JSON',
        error: function () {
            alert('网络错误');
        },
        success: function (res) {
            uptime = res.update_time.substring(11);
            uptime = uptime.substring(0,uptime.length-3);
            $("#city").html(res.city)
            $("#temp").html(res.data[0].wea + ' ' + res.data[0].tem1  + '/' + res.data[0].tem2 )
            console.log('【' + res.city + '】' + res.data[0].wea + ' ' + res.data[0].tem1 + '/' + res.data[0].tem2 + ',' + uptime + '更新~');
    //        $('body').append('【' + res.city + '】' + res.data[0].wea + ' ' + res.data[0].tem1 + '/' + res.data[0].tem2 + ',' + uptime + '更新~');
        }
    });


    // var bigBox = document.getElementById("bigBox");//获取bigBox节点对象
    // var lis = document.querySelectorAll(".controls li");// 获取所有的li节点对象
    // var viewHeight = document.body.clientHeight;//获取当前页面高度
    // var flag = true;//设置开关
    // var index = 0;//设置索引
    //
    // //封装事件,兼容浏览器
    // function on(obj,eventType,fn){
    //     if(obj.addEventListener){
    //         obj.addEventListener(eventType, fn);
    //     }else{
    //         obj.attachEvent("on" + eventType, fn);
    //     }
    // }
    // //鼠标滚动事件处理函数
    // function handler(e){
    //     var _e = window.event || e;
    //     if(flag){
    //         flag = false;
    //         if(_e.wheelDelta==120 || _e.detail==-3){//如果鼠标滚轮向上滚动，detail为火狐判断条件
    //             index--;
    //             if(index<0){
    //                 index = 0;
    //             }
    //         }else{//向下滚动
    //             index++;
    //             if(index>lis.length-1){//如果索引大于页面数，就是滚到最后一张页面时，再滚动鼠标页面不再滚动
    //                 index = lis.length-1;
    //             }
    //         }
    //         bigBox.style.top = -index*viewHeight + "px";//bigBox整体上移index个页面
    //         for(var i=0; i<lis.length; i++){
    //             lis[i].className = "";//重置全部li的类
    //         }
    //         lis[index].className = "active";//设置当前li的类名
    //         setTimeout(function(){//页面滚动间隔一秒，防止滚动太快
    //             flag = true;//重新开启开关
    //         },1000);
    //     }
    // }
    // on(document,"mousewheel",handler);//滚轮滚动事件
    // on(document,"DOMMouseScroll",handler);//滚轮滚动事件，适配火狐浏览器
    // //数字标签点击处理
    // for(var i=0; i<lis.length; i++){
    //     lis[i].tag = i;
    //     lis[i].onclick = function(){
    //         for(var j=0; j<lis.length; j++){
    //             lis[j].className = "";
    //         }
    //         lis[this.tag].className = "active";
    //         bigBox.style.top = (-this.tag*viewHeight) + "px";
    //     }
    // }
});
