let body = document.querySelector('.tweets')

const input = document.getElementById('tweet-input')

const form = document.getElementById('form-tweet') 

var dNone = document.getElementById('err')

form.addEventListener('submit', createTweetHandler) // creating tweets view


function createTweetHandler(e) {
    e.preventDefault()
    const trg = e.target
    const data = new FormData(trg)
    const method = trg.getAttribute('method')
    const url = trg.getAttribute('action')
    const xhr = new XMLHttpRequest()
    let responseType = 'json'
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest') 
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhr.onload = () => {
        var serverResponse = xhr.response

        if(xhr.status === 201){
            input.value = ''
            var newTweetResELm = formatTweets(serverResponse)
            body.innerHTML = newTweetResELm + body.innerHTML 
        }else if(xhr.status === 400){
            var errMsg = serverResponse
            // errorMsg(errMsg)
            console.log(errMsg)
        }else if(xhr.status === 403){
            alert('you must login')
            window.location.href = '/login'
        }
    
    }

    xhr.send(data)
}


function errorMsg(err) {
    dNone.classList.remove('d-none')
    dNone.innerText = err
    setTimeout(()=>{
        dNone.classList.add('d-none')
        dNone.innerText = ''
    }, 3000)
}


let loadTweets = (cls)=>{      // all tweets view.
    const xhr = new XMLHttpRequest()
    let responseType = 'json'
    let method = 'GET'
    const url = 'http://127.0.0.1:8000/api/tweets'
    
    xhr.responseType = responseType
    
    xhr.open(method, url)
    
    xhr.onload = ()=>{
        var serverResponse = xhr.response
        cls.innerHTML = ''
        serverResponse.forEach((element, i) => {
            cls.innerHTML += formatTweets(element)
            
        });
    }
    
    xhr.send()
}

loadTweets(body)


function likesHandler(tweet_id, currentCount){

    alert(`id:${tweet_id} > Likes: ${currentCount}`)

}

function likeBtn(twt){

    return `<button class='btn btn-primary ' onclick='likesHandler(${twt.id}, ${twt.likes})'>${twt.likes} Likes</button>`

}

function formatTweets(tweet){

    var style = `<div class="row bg-sec mb-4 rounded shadow">
                     <div class="col-12 mt-4">
                        <p id=${tweet.id}>${tweet.content}</p4>
                    </div>`
style +=            `<div class="col-12 mb-2 pb-4"> 
                        ${likeBtn(tweet)}
                    </div> 
                </div>`
    return style

}



