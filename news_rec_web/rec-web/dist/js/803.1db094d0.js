"use strict";(self["webpackChunktrade_web"]=self["webpackChunktrade_web"]||[]).push([[803],{1248:function(t,s,e){e.d(s,{A:function(){return c}});var a=function(){var t=this,s=t._self._c;return s("div",{staticClass:"bottomBar"},[s("router-view"),s("van-tabbar",{attrs:{route:""}},[s("van-tabbar-item",{attrs:{icon:"home-o",replace:"",to:"/recLists"}},[t._v("首页")]),s("van-tabbar-item",{attrs:{icon:"friends-o",replace:"",to:"/Myself"}},[t._v("我的")])],1)],1)},i=[],o={name:"bottomBar",data(){return{}},methods:{}},n=o,r=e(845),l=(0,r.A)(n,a,i,!1,null,"699f31ec",null),c=l.exports},803:function(t,s,e){e.r(s),e.d(s,{default:function(){return d}});var a=function(){var t=this,s=t._self._c;return s("div",[s("div",{staticClass:"tabs"},[s("input",{attrs:{type:"radio",id:"tab1",name:"tab-control"}}),s("input",{attrs:{type:"radio",id:"tab2",name:"tab-control",checked:""}}),s("ul",[s("li",{attrs:{title:"Features"},on:{click:t.toRec}},[s("label",{attrs:{for:"tab1",role:"button"}},[s("svg",{attrs:{viewBox:"0 0 24 24"}},[s("path",{attrs:{d:"M14,2A8,8 0 0,0 6,10A8,8 0 0,0 14,18A8,8 0 0,0 22,10H20C20,13.32 17.32,16 14,16A6,6 0 0,1 8,10A6,6 0 0,1 14,4C14.43,4 14.86,4.05 15.27,4.14L16.88,2.54C15.96,2.18 15,2 14,2M20.59,3.58L14,10.17L11.62,7.79L10.21,9.21L14,13L22,5M4.93,5.82C3.08,7.34 2,9.61 2,12A8,8 0 0,0 10,20C10.64,20 11.27,19.92 11.88,19.77C10.12,19.38 8.5,18.5 7.17,17.29C5.22,16.25 4,14.21 4,12C4,11.7 4.03,11.41 4.07,11.11C4.03,10.74 4,10.37 4,10C4,8.56 4.32,7.13 4.93,5.82Z"}})]),s("br"),s("span",[t._v("推荐")])])]),s("li",{staticClass:"hot",attrs:{title:"Delivery Contents"}},[s("label",{staticClass:"hotCont",attrs:{for:"tab2",role:"button"}},[s("svg",{staticClass:"hotPath",attrs:{viewBox:"0 0 24 24"}},[s("path",{attrs:{d:"M2,10.96C1.5,10.68 1.35,10.07 1.63,9.59L3.13,7C3.24,6.8 3.41,6.66 3.6,6.58L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.66,6.72 20.82,6.88 20.91,7.08L22.36,9.6C22.64,10.08 22.47,10.69 22,10.96L21,11.54V16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V10.96C2.7,11.13 2.32,11.14 2,10.96M12,4.15V4.15L12,10.85V10.85L17.96,7.5L12,4.15M5,15.91L11,19.29V12.58L5,9.21V15.91M19,15.91V12.69L14,15.59C13.67,15.77 13.3,15.76 13,15.6V19.29L19,15.91M13.85,13.36L20.13,9.73L19.55,8.72L13.27,12.35L13.85,13.36Z"}})]),s("br"),s("span",[t._v("热门")])])])])]),s("van-pull-refresh",{on:{refresh:t.onRefresh},model:{value:t.isLoading,callback:function(s){t.isLoading=s},expression:"isLoading"}},[s("div",{staticClass:"lists"},[s("van-list",{attrs:{finished:t.finished,"finished-text":t.finishedText,offset:300},on:{load:t.onLoad},model:{value:t.vanListLoading,callback:function(s){t.vanListLoading=s},expression:"vanListLoading"}},t._l(t.$store.state.hotList,(function(e,a){return s("van-cell",{key:a},[s("router-link",{attrs:{to:{name:"NewsInfo",params:{id:e.news_id,likes:e.likes,collections:e.collections,cate:e.cate}}}},[s("div",[s("p",[s("span",{staticClass:"cate"},[t._v(t._s(e.cate))]),s("span",{staticClass:"title"},[t._v(t._s(e.title))])]),s("p",{staticClass:"discribe"},[s("span",{staticClass:"ctime"},[t._v(t._s(e.ctime)+" ")]),s("span",{staticClass:"read_num"},[t._v("阅读："+t._s(e.read_num))]),s("span",{staticClass:"likes"},[t._v("喜欢:"+t._s(e.likes))]),s("span",{staticClass:"collections"},[t._v("收藏:"+t._s(e.collections))])])])])],1)})),1)],1)]),s("bottomBar")],1)},i=[],o=(e(4114),e(1248)),n={name:"hotLists",data(){return{vanListLoading:!1,finished:!1,finishedText:"",scrollTop:0,isLoading:!1}},components:{bottomBar:o.A},mounted(){window.addEventListener("scroll",this.handleScroll,!0)},methods:{onRefresh(){setTimeout((()=>{this.isLoading=!1,this.$store.commit("clearList","hotList"),this.getList()}),1e3)},getList(){let t="/recsys/hot_list?user_id="+this.$store.state.user.username;this.axios.get(t).then((t=>{200===t.data.code&&(this.$store.state.hotList.push(...t.data.data),this.vanListLoading=!1)}))},onLoad(){this.getList()},toRec(){this.$router.push("/recLists")},toHot(){this.$router.push("/hotLists")}},activated(){document.documentElement.scrollTop=this.scrollTop},beforeRouteLeave(t,s,e){"NewsInfo"==t.name&&this.$store.commit("numChange",{item:"hotList",path:t.path}),this.scrollTop=document.documentElement.scrollTop,e()}},r=n,l=e(845),c=(0,l.A)(r,a,i,!1,null,"2feb2560",null),d=c.exports}}]);
//# sourceMappingURL=803.1db094d0.js.map