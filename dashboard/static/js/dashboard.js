var app = new Vue({
    components:{
       dashboardcomponent
    },
    el: '#app',
    data: {
      test:"I'm here!",
      models :[
         {
            name:"Events",
            endpoint:"/api/events/"
         },
         {
            name:"Education",
            endpoint:"/api/education/"
         },
         {
            name:"Media",
            endpoint:"/api/media/"
         },
         {
            name:"Work and Time Logging",
            endpoint:"/api/events/"
         }
      ]
    },
    methods:{
    },
    delimiters:['${','}'],
    created(){
    }
  })

  