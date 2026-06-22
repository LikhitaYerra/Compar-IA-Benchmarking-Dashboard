# GitHub Pages

The static HTML dashboard is published from the `docs/` folder.

- **Live URL:** https://likhitayerra.github.io/Compar-IA-Benchmarking-Dashboard/
- **Source file:** `comparia_dashboard.html` (copied to `docs/index.html` on deploy)

## One-time setup (if Pages is not enabled yet)

1. Open **GitHub → Repository → Settings → Pages**
2. Under **Build and deployment**, set **Source** to **GitHub Actions**
3. Push to `main` — the workflow `.github/workflows/deploy-pages.yml` publishes automatically

## Local preview

Open `comparia_dashboard.html` in any browser, or:

```bash
python3 -m http.server 8080 --directory docs
```

Then visit http://localhost:8080
