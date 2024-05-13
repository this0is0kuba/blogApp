import Blog from "../../models/Blog";
import Comment from "../../models/Comment";
import BlogService from "../../services/BlogService";
import CommentList from "../display/CommentList";
import { useState, useEffect } from "react";
import CommentForm from "../functional/ComentForm";

function BlogDetails({blog} : {blog: Blog}) {

    const [comments, setComments] = useState<Comment[] | null>(null);
    const [isPending, setPending] = useState<boolean>(true);
    const [error, setError] = useState<Error | null>(null);

    function handleCommentEvent(newComment: Comment) {
        setComments([newComment, ...comments!]);
        console.log("no siema byku")
    }

    useEffect( () => {

        const blogService = BlogService.getBlogService();

        blogService.getCommentByBlogId(blog.id)
            .then( (data: Comment[]) => {
                setComments(data) 
                setPending(false)
                setError(null);
            })
            .catch( (err: Error) => {
                setError(err);
                setPending(false);
            })

    }, [blog.id]);

    return (
        <div className="bg-dark p-3 mt-2 rounded">

            <div className="d-flex justify-content-between align-items-center pt-3 ">
                <div>
                    <h1 className="m-0">{blog.title}</h1>
                    <p><small className="" >{blog.creationDate}</small></p>
                </div>

                <div>
                    <h4 className="p-2">Author: <b className="text-warning">{blog.author.username}</b></h4>
                </div>
            </div>

            <p className="p-2 mt-3 rounded border">{blog.content}</p>

            <div className="mb-5">
                <span >Category: <b>{blog.category}</b></span>
            </div>

            <hr></hr>
            <h4 className="my-3">Comment Section</h4>

            {error && <h2>{error.message}</h2>}
            {isPending && <h2>Loading...</h2>}
            {comments && <CommentForm blogId={blog.id} handleCommentEvent={handleCommentEvent} 
                                      maxCommentId={Math.max(...comments!.map( (c) => c.id ))}/>}
            {comments && <CommentList comments={comments}/>}

        </div>
    );
}

export default BlogDetails;