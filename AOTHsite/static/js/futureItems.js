const futureItems = {
    template:
    `
    <template>
      <div class = "futureItems" v-if="futureItems.length > 0">
         <record v-for="item in futureItems" :record="item" :model="model"/>
      </div>
      <span v-else>Nothing coming up</span>
    </template>
    `,
    data(){
       return{
 
       }
    },
    props:['futureItems','model'],
    components:{
      record
  }
 }