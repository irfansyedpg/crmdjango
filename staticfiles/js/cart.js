

var updateBtns=document.getElementsByClassName('update-cart')

for(var i=0;i<updateBtns.length;i++)
{

    updateBtns[i].addEventListener('click',function()
    {

        var productId=this.dataset.product
        var action=this.dataset.action

        console.log('productid:',productId,'actioin:',action)

        console.log('User:',user)

        if(user=='AnonymousUser')
        {
           addCookieItem(productId,action)
        

        }
        else{
            updateUserOrder(productId,action)
        }
    })
}


function addCookieItem(productId,actioin)
{
    console.log('not logged in')

    if(actioin == 'add')
    {
        if(cart[productId] == undefined) // remember we have created cart object in main html JS
        {
            cart[productId] = {'quantity':1}
        }
        else
        {
            cart[productId]['quantity']+=1
        }
    }
    if(actioin == 'remove')
    {
        cart[productId]['quantity']-=1
        
        if(cart[productId]['quantity'] <= 0)
        {
            console.log('remove item')
            delete cart[productId]
        }
    }

    console.log('Cart:',cart)
    document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()


}


function updateUserOrder(productId,action)
{

    console.log('function user logged in , sending data ')

    var url='/update_item/' // you URL in the ulr file for calling the view 

    fetch(url,{   // fetch API for interaction with view and sending data POST request 
  
        method:'POST',
        headers:{'Content-Type':'application/json',
        'X-CSRFToken':csrftoken
    
    },
        body: JSON.stringify( { // we need to send data in string formate
            'productId':productId,
            'action':action
        } )

        } )

        .then ( (response) =>{ // this is for the response when the action completed in the view whatever return it will displayed here
            return response.json()


        }) 

        .then ( (data) =>{ // this is for the response when the action completed in the view whatever return it will displayed here
            
            console.log('data:',data)
            location.reload() // reload the page for show number of stock in the icons 


        }) 


}



 