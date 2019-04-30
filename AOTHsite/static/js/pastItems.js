const pastItems = {
    template:
    `
    <div class = "pastItems">
       <record v-for="item in pastItems" :record="item" :model="model"/>
   </div>
    `,
    data(){
       return{
       }
    },
    methods:{
    },
    props:['pastItems','model'],
    components:{
        record
    }
 }