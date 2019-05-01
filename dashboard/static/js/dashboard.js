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
            name:"promotion",
            endpoint:"/api/promotion/"
         },
      ]
    },
    methods:{
    },
    delimiters:['${','}'],
    created(){
    }
  })

  