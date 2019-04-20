const record = {
    template:
    `
    <div class = "row text-white bg-primary py-1">
    <div class = "col-sm-6">
    <span>
    <a :href="'/'+model+'/'+record.url" target = "_blank"> 
       {{record.name}}
    </a>
    </span>
    </div>
    <div class = "col-sm-6">
     {{record.date }}
    </div>
    </div>
    `,
    props:['record','model']
 }