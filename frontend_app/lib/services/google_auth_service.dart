import 'package:google_sign_in/google_sign_in.dart';

class GoogleAuthService {
  static final GoogleSignIn _googleSignIn = GoogleSignIn(
    clientId: "658312207862-1atk3gothavrp390c09o3sk96h0q8ott.apps.googleusercontent.com",
    scopes: ['email', 'profile', 'openid'],
  );

  static Future<String?> getIdToken() async {
    try {
      final GoogleSignInAccount? user = await _googleSignIn.signIn();
      if (user == null) return null;

      final auth = await user.authentication;
      return auth.idToken;
    } catch (e) {
      print("Google Error: $e");
      return null;
    }
  }

  static Future<void> signOut() async {
    await _googleSignIn.signOut();
  }
}
