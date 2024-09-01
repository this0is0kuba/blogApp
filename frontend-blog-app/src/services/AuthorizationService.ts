import Token from "../models/Token";

class AuthorizationService {

    private static instance: AuthorizationService;
    private readonly authorizationURL: string = "http://localhost:8000/token";
    private token: Token | null = null;

    private constructor() {}

    public static getAuthorizationService(): AuthorizationService {
        
        if(AuthorizationService.instance === undefined)
            AuthorizationService.instance = new AuthorizationService();

        return AuthorizationService.instance;
    }

    public async authorizeUser(email: string, password: string): Promise<Token | null> {

        await new Promise(resolve => setTimeout(resolve, 1000));

        const urlSearchParams = new URLSearchParams();
        urlSearchParams.append('username', email);
        urlSearchParams.append('password', password);
        
        const response = await fetch(this.authorizationURL,
            {
                method: "POST",
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: urlSearchParams
            }
        );

        if(!response.ok)
            throw new Error('Could not fetch the data for that resource')

        const data = await response.json();
        this.token = {
            tokenType: data.token_type,
            accessToken: data.access_token
        }

        return this.token;
    }

    public getToken(): Token | null {
        return this.token;
    }

}

export default AuthorizationService