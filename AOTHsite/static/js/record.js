const record = {
    template:
    `
    <div class = "d-flex border py-1">
    <div class = "mx-3">
    <span>
    <a :href="'/'+model+'/'+record.url" target = "_blank"> 
       {{record.name}}
    </a>
    </span>
    </div>
    <div>
     {{record.date }}
    </div>
    </div>
    `,
    props:['record','model']
 }