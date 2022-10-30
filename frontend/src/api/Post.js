import axios from 'axios'


export function getInbox(){
    const url = `http://localhost:8000/authors/${localStorage.getItem("authorID")}/inbox/` // has to be userID


    return axios.get(url, {
        headers:{
            "Content-Type": "application/json",
            Authorization: `JWT ${localStorage.getItem("access_token")}`
        }
    }).then((response) =>{
        return response;
    }).catch((error)=>{
        return error.response;
    })
}

export function test(){
    const url = 'http://127.0.0.1:8000/authors/' // has to be userID


    return axios.get(url, {
        headers:{
            "Content-Type": "application/json",
            Authorization: `JWT ${localStorage.getItem("access_token")}`
            // authorization?
        }
    }).then((response) =>{
        return response;
    }).catch((error)=>{
        
        return error.response;
    })
}

export function getPost(){
    const url = 'http://127.0.0.1:8000/authors/7/posts'

    return axios.get(url, {
        headers:{
            "Content-Type": "application/json",
            Authorization: `JWT ${localStorage.getItem("access_token")}`
            // authorization?
        }
    }).then((response) =>{
        return response;
    }).catch((error)=>{
        
        return error.response;
    })
}

export function getPostByID(post_id) {
    const url = `http://localhost:8000/posts/${post_id}/`
    return axios.get(url, {
        headers:{
            "Content-Type": "application/json",
            Authorization: `JWT ${localStorage.getItem("access_token")}`
        }
    }).then((response) =>{
        // console.log("returning response");
        // console.log(response.data);
        return response;
    }).catch((error)=>{
        return error.response;
    })
}
 

export function postPost(param = {}){
    const url = 'http://127.0.0.1:8000/posts'

    const body = {
        title: param.title,
        description: param.description,
        content: param.content,
        visibility: param.visibility,
        unlisted: param.unlisted
    }

    return axios.post(url, body, {
        headers:{
            "Content-Type": "text/plain",
            Authorization: `JWT ${localStorage.getItem("access_token")}`
        }
    }).then((response) =>{
        return response;
    }).catch((error)=>{
        
        return error.response;
    })
}