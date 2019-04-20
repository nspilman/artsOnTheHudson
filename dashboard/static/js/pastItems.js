const pastItems = {
    template:
    `
    <div class = "pastItems" v-if="pastItems.length > 0">
    <h1 style="cursor:pointer; border-radius:1em;" @click="show=!show" class = "bg-secondary p-1 text-white w-50">Past Shit </h1>
       <record v-if="show" v-for="item in pastItems" :record="item" :model="model"/>
   </div>
    `,
    data(){
       return{
         show:false,
       }
    },
    methods:{
    },
    props:['pastItems','model'],
    components:{
        record
    }
 }