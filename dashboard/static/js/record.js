const record = {
    template:
    `
    <div class = "row text-white bg-primary py-1">
    <div class = "col-sm-6">
    <span> 
       {{record.name}}
    </span>
    </div>
    <div class = "col-sm-6">
     {{record.date }}
    </div>
    </div>
    `,
    props:['record']
 }