import Blog from "../models/Blog";
import fetchWithAuth from "./ApiService";

class BlogService {

    private static instance: BlogService;
    private static readonly blogURL: string = "http://localhost:8000/blogs/";
    private static readonly commentURL: string = "http://localhost:8000/comments/"; 
    private static blogList: Blog[];

    private constructor() {}

    public static getBlogService(): BlogService {
        
        if(BlogService.instance == null)
            BlogService.instance = new BlogService();

        return BlogService.instance;
    }

    public async getBlogs(): Promise<Blog[]> {

        await new Promise(resolve => setTimeout(resolve, 1000));

        if(!BlogService.blogList) {

            const response = await fetch(BlogService.blogURL);

            if(!response.ok)
                throw new Error('Could not fetch the data for that resource')

            const data: Blog[] = await response.json();
            BlogService.blogList = data;
        }
        
        return Promise.resolve(BlogService.blogList);
    }

    public async getBlog(id: number) {

        await new Promise(resolve => setTimeout(resolve, 1000));

        const response = await fetchWithAuth(BlogService.blogURL + id);

        if(!response.ok)
            throw new Error('Could not fetch the data for that resource')

        return response.json();
    }

    public async getCommentsByBlogId(blogId: number) {

        await new Promise(resolve => setTimeout(resolve, 1000));

        const response = await fetch(BlogService.commentURL);

        if(!response.ok)
            throw new Error('Could not fetch the data for that resource')

        return response.json();
    }
}

export default BlogService;