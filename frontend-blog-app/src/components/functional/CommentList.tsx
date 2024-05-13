import Comment from "../../models/Comment";

function CommentList( {comments}: {comments: Comment[]} ) {
    return (
        <div>
            <form className="row g-3 justify-content-md-center">
                <div className="col-8">
                    <textarea className="form-control" rows={2} id="inputPassword2" placeholder="add comment"></textarea>
                </div>
                <div className="col-2">
                    <button type="submit" className="btn btn-primary mb-3 h-100">Add comment</button>
                </div>
            </form>    
            {
                comments.map( (comment: Comment) => (
                    <div key={comment.id} className="rounded p-2 m-2 border-bottom">
                        <h6 className="text-info"><b>{comment.author.username}</b></h6>
                        <p>{comment.content}</p>
                    </div>    
                ))
            }
        </div>
    );
}

export default CommentList;