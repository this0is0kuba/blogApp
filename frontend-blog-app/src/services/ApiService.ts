import Token from "../models/Token";
import AuthorizationService from "./AuthorizationService"

const fetchWithAuth = async (url: string, options: RequestInit = {}) => {

    const authService: AuthorizationService = AuthorizationService.getAuthorizationService();
    const token: Token | null = authService.getToken();

    if(!token)
        throw new Error("You have tried to send request without token");

    const authOptions = { ...options };

    authOptions.headers = {
        ...authOptions.headers,
        Authorization: `${token.tokenType} ${token.accessToken}`,
    };

    return await fetch(url, authOptions);
}

export default fetchWithAuth