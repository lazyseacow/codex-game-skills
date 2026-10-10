# Security Policy

Security fixes target the `main` branch. Report confirmed vulnerabilities using
[GitHub private vulnerability reporting](https://github.com/lazyseacow/codex-game-skills/security/advisories/new)
when available. Include the affected file, reproduction steps and impact.

This collection contains local instructions and executable helpers. Relevant
issues include undisclosed command execution, secret exposure, prompt injection
in contributed instructions, and changes that exceed user-authorized scope.
Host permissions and sandbox settings remain controlled by Codex.

Contributions must document outbound requests and required environment access,
preserve user authorization, and avoid credentials or local settings in commits.
Use portable Bash supported on Linux and macOS. Review executable changes and
validate commands against the intended workspace before publishing them.
