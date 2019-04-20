const dashboardcomponent =  {
    template: `
    <div class = "card p-4">
            <h2> 
             {{model.name}}
            </h2>
            <pastItems :pastItems="pastRecords"/>
        </div>`,
    data(){
        return{
           records:null,
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
          pastItems
        }
    }