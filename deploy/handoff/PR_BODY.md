## Summary

Adds build-time checks and a CSP snippet for production:

- `scripts/check-debug-bundle.sh` fails the build if debug markers (`stability-debug`, `initDebug`, `__DEBUG__` by default) appear in `dist/`.
- `.github/workflows/build-check.yml` runs `npm ci`, the production build, and the debug check on pushes to `main` and on pull requests.
- `deploy/nginx-csp.conf` is a CSP header snippet. A `location` block with its own `add_header` overrides the server-level one, so repeat it there.
- `.gitattributes` keeps `*.sh` as LF so scripts run in Linux containers.

## Reviewer notes

- The workflow assumes an npm project with a `build` script that outputs to `dist/`. Adjust the paths if the project differs.
- The check looks only for the debug markers. It doesn't grep for `console.log`, because Terser's `drop_console` already removes those calls.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
