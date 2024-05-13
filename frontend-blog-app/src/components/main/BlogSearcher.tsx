import { useEffect, useState } from "react";
import BlogService from "../../services/BlogService";
import BlogList from "../display/BlogList";
import Blog from "../../models/Blog";

function BlogSearcher() {

    const [blogs, setBlogs] = useState<Blog[]>([]);
    const [isPending, setPending] = useState<boolean>(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        
        const blogService = BlogService.getBlogService();

        blogService.getBlogs()
            .then( (data: Blog[]) => {
                setBlogs(data) 
                setPending(false)
                setError(null);
            })
            .catch( (err: Error) => {
                setError(err);
                setPending(false);
            })

    }, []);

    return (    
        <div>
            {error && <h2>{error.message}</h2>}
            {isPending && <h2>Loading...</h2>}
            {blogs && <BlogList blogs={blogs} />}
        </div>
    );
}

export default BlogSearcher;