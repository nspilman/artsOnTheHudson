var app = new Vue({
    components:{
       dashboardcomponent
    },
    el: '#app',
    data: {
      test:"I'm here!",
      models :[
         {
            name:"events",
            endpoint:"/api/events/"
         },
         {
            name:"education",
            endpoint:"/api/education/"
         },
         {
            name:"media",
            endpoint:"/api/media/"
         },
      ]
    },
    methods:{
    },
    delimiters:['${','}'],
    created(){
    }
  })

  