const dashboardcomponent =  {
    template: `
    <div class = "card p-4">
      <div v-if="pastRecords.length > 0"  class = "row">
         <div class = "col-sm-6">
            <h2> 
             {{model.name}}
            </h2>
         </div>
         <div class = "col-sm-6">
            <button class = "btn w-100" style="font-size:10px;" @click="togglePastFuture"> 
               {{futureOrPast}} <br>{{model.name}}
            </button>
         </div>   
         <pastItems v-if="past" :pastItems="pastRecords" :model = "model.name"/>
      </div>
      <div v-else class = "row">
         <div class = "col-sm-12">
         <h2> 
         {{model.name}}
        </h2>
         </div>
      </div>
      <futureItems v-if="futureOrPast=='past'" :futureItems="futureRecords" :model="model.name"/>
   </div>`,
    data(){
        return{
           records:null,
           past:false,
           futureOrPast:"past"
          }
    },
    props:['model'],
    computed:{
        },
        methods:{
           async getRecords(){
                const resp =  await axios.get(this.model.endpoint)
                const data = await resp.data
                const records = await data.map(record => JSON.parse(record))
                this.records = records
             },
             togglePastFuture(){
                if(this.futureOrPast == "future"){
                   this.futureOrPast = "past"
                }
                else{
                   this.futureOrPast = "future"
                }
                this.past = !this.past
             }
            },
        created(){
           this.getRecords()
        },
        computed:{
          pastRecords(){
            if(this.records)
            return this.records.filter(record => new Date(record.date) < new Date())

          },
          futureRecords(){
             return this.records.filter(record => new Date(record.date) > new Date())  
          }
        },
        components:{
          pastItems,
          futureItems
        }
    }