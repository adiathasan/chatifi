let body = document.querySelector('.tweets')

const input = document.getElementById('tweet-input')

const form = document.getElementById('form-tweet') 

var dNone = document.getElementById('err')

// CSRF-to send it to backend
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

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
        }else if (xhr.status === 401){
            console.log(serverResponse)
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


function likesHandler(tweet_id, currentCount, action){
    console.log(tweet_id, currentCount)
    var url = 'tweet/action'
    const method = 'POST'
    const data = JSON.stringify({
        id : tweet_id,
        action: action
     })

    var xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.setRequestHeader('Content-Type', 'application/json')
    xhr.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest')
    xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    xhr.setRequestHeader('X-CSRFToken', csrftoken)
    xhr.onload = ()=>{
       
        loadTweets(body)
  
    }

    xhr.send(data)

}

function likeBtn(twt){

    if(twt.like > 1){
        return `<button class='btn btn-primary btn-sm ' onclick='likesHandler(${twt.id}, ${twt.like}, "like")'>${twt.like} Likes</button>`
    }

    return `<button class='btn btn-primary btn-sm' onclick='likesHandler(${twt.id}, ${twt.like}, "like")'>${twt.like} Like</button>`

}

function ReTweetBtn(twt) {

    return `<button class='btn btn-outline-dark btn-sm' onclick='likesHandler(${twt.id}, ${twt.like}, "retweet")'>ReTweet</button>`

}


function UnLiketBtn(twt) {

    return `<button class='btn btn-outline-light btn-sm' onclick='likesHandler(${twt.id}, ${twt.like}, "unlike")'> Unlike</button>`

}



function formatTweets(tweet){

    var style = `<div class="row bg-sec mb-4 rounded shadow">
                     <div class="col-12 mt-4">
                        <p id=${tweet.id}>${tweet.content}</p4>
                    </div>`
style +=            `<div class="col-12 mb-2 pb-4"> 
                        ${likeBtn(tweet)}
                        ${UnLiketBtn(tweet)}
                        ${ReTweetBtn(tweet)}
                    </div> 
                </div>`
    return style

}



