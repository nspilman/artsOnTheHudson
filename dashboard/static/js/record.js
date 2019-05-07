const record = {
    template: 
    `
    <div>
    <div class = "d-flex py-1 w-100" @mouseover="hover=!hover" @mouseleave="hover=!hover" style ="-webkit-user-select: none;user-select: none; display:block;">
      <div class = "mx-3">
         <span>
         <a :href="'/'+model+'/'+record.url" target = "_blank"> 
            {{record.name}}
         </a>
         </span>
      </div>
      <div class>
         {{record.date }}
      </div>
      <div class = "p-1">
      <a :href="'/admin/website/'+model+'/'+record.id" target = "_blank"> 
         <i class="fas fa-edit"></i>
      </a>
      </div>
      </div>
    `,
    props:['record','model'],
    data(){
       return{
          hover:false,
       }
    },
    created(){
       }
    }