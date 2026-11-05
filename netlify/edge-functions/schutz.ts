// Schützt die ganze Seite mit einem gemeinsamen Passwort (Netlify-Umgebungsvariable SEITEN_PASSWORT).
// Ohne gesetzte Variable bleibt die Seite gesperrt.
import type { Context } from "https://edge.netlify.com";

export default async (req: Request, context: Context) => {
  const passwort = Netlify.env.get("SEITEN_PASSWORT");
  if (!passwort) return new Response("Noch nicht eingerichtet.", { status: 503 });
  const kopf = req.headers.get("authorization") || "";
  if (kopf.startsWith("Basic ")) {
    try {
      const [, pw] = atob(kopf.slice(6)).split(/:(.*)/s);
      if (pw === passwort) return context.next();
    } catch (_) { /* ungültig */ }
  }
  return new Response("Anmeldung erforderlich.", {
    status: 401,
    headers: { "WWW-Authenticate": 'Basic realm="enneo Wettbewerb", charset="UTF-8"' },
  });
};

export const config = { path: "/*" };
