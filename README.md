# Sandboxing AI coding agents

This repository contains a Quarto/RevealJS presentation about where the security boundary of an AI coding-agent sandbox should end.

The presentation is based on two blog posts:

- [Where should an AI agent's sandbox end?](https://www.samrickman.com/blog/ai-agent-sandboxes)
- [How a sandboxed agent left code for my host to execute](https://www.samrickman.com/blog/ai-agent-sbx-clone-vs-direct-execute)

It covers two questions:

1. Whether a sufficiently isolated Docker sandbox makes it reasonable to run an agent with permission prompts disabled.
2. Whether agent-authored code can still cross the sandbox boundary and later execute on the host.

The deck explores Docker Sandboxes network and workspace policies, briefly mentions Claude Code sandboxes, uses the "lethal trifecta" as a way to think about prompt-injection/exfiltration risk, and includes an interactive comparison of different sandbox policies.

## Rendering

The deck is written in Quarto and rendered with RevealJS. From the repository root:

```bash
quarto render ai-agent-sandboxing-gds.qmd
```

The presentation expects the accompanying theme, images and interactive HTML assets to remain at the relative paths used by the QMD file.

## References

- Rickman, S. [Where should an AI agent's sandbox end?](https://www.samrickman.com/blog/ai-agent-sandboxes).
- Rickman, S. [How a sandboxed agent left code for my host to execute](https://www.samrickman.com/blog/ai-agent-sbx-clone-vs-direct-execute).
- Fan, H., Wang, X., Chu, Z., Wang, Q., Wang, Z., Liu, M., Qin, B., & XingYu. (2026). [LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?](https://arxiv.org/abs/2605.28721).
- Willison, S. (2025). [The lethal trifecta for AI agents: private data, untrusted content, and external communication](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).
- Docker. [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/), [default security posture](https://docs.docker.com/ai/sandboxes/security/defaults/), [local/network policy](https://docs.docker.com/ai/sandboxes/governance/access-controls/local/), and [Git workflows](https://docs.docker.com/ai/sandboxes/workflows/git/).
- Anthropic. [Claude Code sandboxing](https://code.claude.com/docs/en/sandboxing).