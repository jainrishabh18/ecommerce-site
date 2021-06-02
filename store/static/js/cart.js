var updateBtns = document.getElementsByClassName('update-cart')
//here we are adding  addd to cart fucntionality by clicking on add to 
//cart that product will be added to the cart
for(i=0; i < updateBtns.length; i++)
{
    updateBtns[i].addEventListener('click',function(){

        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId , 'Action:',action)
//user authentication code is written below whether user 
//is logged in or not
        console.log('USER:',user)
        if(user === 'AnonymousUser'){
            console.log('User not logged in')
        }
        else{
            updateUserOrder(productId,action)
        }
    })
}
function updateUserOrder(productId,action){
    console.log('User is authenticated, sending data...')

    //It is url where it send post deta to
    var url = '/update_item/'
    //The Fetch API interface allows web browser to make HTTP requests to web servers.
    fetch(url,{
        method : 'POST',
        headers :{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId ,'action':action})

    })
    // The then () method returns a Promise. It takes two arguments: callback
    // functions for the success and failure cases of the Promise.
    .then((response)=>{
        return response.json();//JSON is a syntax for storing and exchanging data
    })

    .then((data)=>{
        console.log('Data:',data)
    });


}