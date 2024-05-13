import { FormEvent, useState } from "react";
import Comment from "../../models/Comment";

function CommentForm( {blogId, handleCommentEvent, maxCommentId}: {blogId: number, handleCommentEvent: Function, maxCommentId: number} ) {

    const [content, setContent] = useState<string>('');

    function handleSubmit(e: FormEvent<HTMLFormElement>) {

        e.preventDefault();

        var currentDate = new Date();

        var year = currentDate.getFullYear();
        var month = currentDate.getMonth() + 1;
        var day = currentDate.getDate();

        var formattedDate = year + '-' + (month < 10 ? '0' + month : month) + '-' + (day < 10 ? '0' + day : day);

        maxCommentId ++;

        const newComment: Comment = {
                                        id: maxCommentId, content: content, creationDate: formattedDate, blogId: blogId, 
                                        author: {id: -1, username: "noname", email: "noname@wp.pl", role: ["user"]}}

        console.log(newComment);
        handleCommentEvent(newComment);
    }

    return (

        <form className="row g-3 justify-content-md-center" onSubmit={ (e) => handleSubmit(e)}>
            <div className="col-8">
                <textarea className="form-control" value={content} onChange={ (e) => setContent(e.target.value)} rows={2} id="inputPassword2" placeholder="Nice Blog!"></textarea>
            </div>
            <div className="col-2">
                <button type="submit" className="btn btn-primary mb-3 h-100">Add comment</button>
            </div>
        </form>    

    );
}

export default CommentForm;