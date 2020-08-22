let body = document.querySelector('.tweets')

const input = document.getElementById('tweet-input')

const form = document.getElementById('form-tweet') 

form.addEventListener('submit', createTweetHandler)


function createTweetHandler(e) {
    e.preventDefault()
    const trg = e.target
    const data = new FormData(trg)
    const method = trg.getAttribute('method')
    const url = trg.getAttribute('action')
    const xhr = new XMLHttpRequest()

    xhr.open(method, url)

    xhr.onload = () => {
        var serverResponse = xhr.response
        input.value = ''
        loadTweets(body)
    }

    xhr.send(data)
}


let loadTweets = (cls)=>{
    const xhr = new XMLHttpRequest()
    let responseType = 'json'
    let method = 'GET'
    const url = 'http://127.0.0.1:8000/api/tweets'
    
    xhr.responseType = responseType
    
    xhr.open(method, url)
    
    xhr.onload = ()=>{
        var serverResponse = xhr.response
        cls.innerHTML = ''
        serverResponse.response.forEach((element, i) => {
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

    var style = `<div class="row bg-sec mb-2 rounded">
                     <div class="col-12 mt-4">
                        <p id=${tweet.id}>${tweet.content}</p4>
                    </div>`
style +=            `<div class="col-12 mb-2 pb-4"> 
                        ${likeBtn(tweet)}
                    </div> 
                </div>`
    return style

}



