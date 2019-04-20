const pastItems = {
    template:
    `
    <ul>
       <li v-for="item in pastItems">{{item.name}}</li>
    </ul>
 
    `,
    data(){
       return{
 
       }
    },
    props:['pastItems']
 }