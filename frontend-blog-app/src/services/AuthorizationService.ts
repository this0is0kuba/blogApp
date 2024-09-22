import Token from "../models/Token";
import { clientId } from "../secret";

class AuthorizationService {

    private static instance: AuthorizationService;
    private readonly authorizationURL: string = "http://localhost:8000/token";
    // Google's OAuth 2.0 endpoint for requesting an access token
    private readonly oauth2Endpoint: string = 'https://accounts.google.com/o/oauth2/v2/auth';
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

    public async oauthSignIn(): Promise<void> {

        // Parameters to pass to OAuth 2.0 endpoint
        const params = new URLSearchParams({
            client_id: clientId,
            redirect_uri: 'http://localhost:3000/GoogleCallback',
            response_type: 'token',
            scope: 'https://www.googleapis.com/auth/drive.metadata.readonly',
            include_granted_scopes: 'true',
            state: 'pass-through value'
        });

        window.localStorage.setItem('state', 'pass-through value');

        window.location.replace(`${this.oauth2Endpoint}?${params.toString()}`)
    }

}

export default AuthorizationService