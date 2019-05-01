const dashboardcomponent =  {
    template: `
    <div class = "card p-4 border text-white bg-dark border-dark" style="border-radius:20px;">
      <div v-if="pastRecords.length > 0"  style="display:flex; justify-content:space-between;">
            <h2 class="text-white"> 
             {{model.name.toUpperCase()}}
            </h2>
         <div class = "col-sm-4" class="text-white">
            <button class = "btn w-100 text-white" style="font-size:10px;" @click="togglePastFuture"> 
               {{futureOrPast}} <br>{{model.name}}
            </button>
         </div>   
         </div>
         <pastItems v-if="past" :pastItems="pastRecords" :model = "model.name"/>
      <div v-else class = "row">
         <div class = "col-sm-12 text-center text-white" v-if="pastRecords.length == 0">
         <h2 class="text-white"> 
         {{model.name.toUpperCase()}}
        </h2>
         </div>
      </div>
      <div style="display:flex;justify-content:center;">
      <a :href="'/admin/website/'+model.name+'/add/'" target="_blank">
         <button class = " border border-primary m-1">
            <h4 class="mb-0 text-white">Create New {{model.name}} </h4>
         </button>
      </a>
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
                const data = await resp.data;
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
            if(this.records){
            return this.records.filter(record => new Date(record.date) < new Date())
            }
            else{
               return [];
            }
          },
          futureRecords(){
             return this.records.filter(record => (new Date(record.date) > new Date() || !record.date)) 
          }
        },
        components:{
          pastItems,
          futureItems
        }
    }