# Custom Domain Setup Guide

Complete guide to configure `rodrigallardo.art` for your GitHub Pages site.

## ✅ Code Changes (Already Done)

All code changes have been completed:
- ✅ Updated `astro.config.mjs` (site URL and base path)
- ✅ Created `public/CNAME` file
- ✅ Updated all page URLs and image paths
- ✅ Updated navigation and language switching logic
- ✅ Build tested successfully

## 📋 What You Need To Do

You need to configure **two things**:
1. **GitHub Repository Settings** (enable custom domain)
2. **Squarespace DNS Settings** (point domain to GitHub)

---

## Part 1: GitHub Repository Configuration

### Step 1: Merge and Deploy Code Changes

```bash
# Merge feature branch to main
git checkout main
git merge feature/custom-domain-setup
git push origin main
```

Wait for GitHub Actions deployment to complete (~30 seconds).

### Step 2: Configure Custom Domain in GitHub

1. **Go to your repository on GitHub:**
   https://github.com/rodrigallardo/web-portfolio

2. **Navigate to Settings:**
   - Click **Settings** tab at the top
   - Scroll down to **Pages** section (left sidebar)

3. **Configure Custom Domain:**
   - Under "Custom domain", enter: `rodrigallardo.art`
   - Click **Save**

4. **Wait for DNS Check:**
   - GitHub will check DNS configuration
   - You'll see "DNS check in progress" initially
   - This will fail UNTIL you configure Squarespace DNS (Part 2)

5. **Enable HTTPS (After DNS works):**
   - Once DNS check passes, check the box:
     ☑️ **Enforce HTTPS**
   - This provides SSL certificate (https://)

---

## Part 2: Squarespace DNS Configuration

### Option A: Using A Records + CNAME (Recommended)

This setup works with the apex domain (rodrigallardo.art) and www subdomain.

#### Step 1: Login to Squarespace Domains

1. Go to your Squarespace account
2. Navigate to **Settings** → **Domains**
3. Click on **rodrigallardo.art**
4. Go to **DNS Settings** or **Advanced Settings**

#### Step 2: Add A Records

Add **4 A records** pointing to GitHub's IP addresses:

| Type | Name/Host | Value/Points To | TTL |
|------|-----------|-----------------|-----|
| A | @ | 185.199.108.153 | 3600 |
| A | @ | 185.199.109.153 | 3600 |
| A | @ | 185.199.110.153 | 3600 |
| A | @ | 185.199.111.153 | 3600 |

**Note:**
- `@` represents the root domain (rodrigallardo.art)
- Some DNS interfaces use "blank" or "@" for the root
- TTL (Time To Live) can be 3600 seconds (1 hour)

#### Step 3: Add CNAME Record (Optional but Recommended)

Add a CNAME record for the www subdomain:

| Type | Name/Host | Value/Points To | TTL |
|------|-----------|-----------------|-----|
| CNAME | www | rodrigallardo.github.io | 3600 |

This makes `www.rodrigallardo.art` redirect to `rodrigallardo.art`.

#### Step 4: Remove Conflicting Records (If Any)

If you see existing A or CNAME records for `@` or `www`, you may need to:
- **Delete** old A records pointing elsewhere
- **Delete** CNAME for @ (can't have both A and CNAME for root)
- Keep only the 4 GitHub A records and the www CNAME

---

### Option B: Using CNAME Only (Alternative)

If Squarespace doesn't support A records for apex domain, use CNAME flattening:

| Type | Name/Host | Value/Points To | TTL |
|------|-----------|-----------------|-----|
| CNAME | @ | rodrigallardo.github.io | 3600 |
| CNAME | www | rodrigallardo.github.io | 3600 |

**Note:** Not all DNS providers support CNAME for apex (@). Try Option A first.

---

## Part 3: Verification & Testing

### 1. DNS Propagation Check

DNS changes can take **24-48 hours** to propagate worldwide, but often work in **10-30 minutes**.

**Check DNS status:**
```bash
# Check if A records are set
dig rodrigallardo.art

# Check if www CNAME is set
dig www.rodrigallardo.art
```

Or use online tools:
- https://dnschecker.org
- https://mxtoolbox.com/SuperTool.aspx

### 2. GitHub Pages DNS Check

1. Go back to GitHub Settings → Pages
2. Refresh the page
3. Check if DNS check passes:
   - ✅ **"DNS check successful"** → You're good!
   - ❌ **"DNS check failed"** → Wait longer or check DNS settings

### 3. Test Your Site

Once DNS check passes:

1. Visit: http://rodrigallardo.art
2. Visit: https://rodrigallardo.art (after enabling HTTPS)
3. Visit: http://www.rodrigallardo.art (should redirect)

### 4. Enable HTTPS

Once the site loads via http:
1. Go to GitHub Settings → Pages
2. Check: ☑️ **Enforce HTTPS**
3. Wait a few minutes for SSL certificate provisioning
4. Visit: https://rodrigallardo.art

---

## Troubleshooting

### "DNS check failed" in GitHub

**Possible causes:**
- DNS not propagated yet (wait 30 minutes to 24 hours)
- A records not configured correctly
- Wrong IP addresses
- Squarespace blocking external DNS

**Solutions:**
1. Double-check all 4 A record IP addresses
2. Wait longer (DNS can be slow)
3. Clear your browser cache
4. Try incognito/private browsing mode

### Site shows 404 error

**Possible causes:**
- Deployment hasn't finished
- CNAME file missing (should be in `public/CNAME`)
- Base path incorrect

**Solutions:**
1. Check GitHub Actions: https://github.com/rodrigallardo/web-portfolio/actions
2. Verify CNAME file exists in repository
3. Wait for deployment to complete

### Old GitHub Pages URL still works

**This is normal!** Both URLs will work:
- ✅ https://rodrigallardo.github.io/web-portfolio (old, still works)
- ✅ https://rodrigallardo.art (new custom domain)

If you want ONLY the custom domain to work, enable "Enforce HTTPS" in GitHub Pages settings.

### Images not loading

**Possible cause:**
- Browser cached old URLs with `/web-portfolio` prefix

**Solution:**
- Hard refresh: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Clear browser cache
- Try incognito/private mode

---

## DNS Records Summary

For quick reference, here's what your Squarespace DNS should look like:

```
Type    Name/Host    Value/Points To          TTL
----    ---------    -------------------      ----
A       @            185.199.108.153          3600
A       @            185.199.109.153          3600
A       @            185.199.110.153          3600
A       @            185.199.111.153          3600
CNAME   www          rodrigallardo.github.io  3600
```

---

## Expected Timeline

- **Code deployment:** ~30 seconds (GitHub Actions)
- **DNS propagation:** 10 minutes to 24 hours (usually ~30 min)
- **SSL certificate:** 5-15 minutes (after DNS works)
- **Total time:** 15 minutes to 24 hours

---

## Need Help?

If you encounter issues:

1. **Check GitHub Actions logs:**
   https://github.com/rodrigallardo/web-portfolio/actions

2. **Verify DNS propagation:**
   https://dnschecker.org (enter `rodrigallardo.art`)

3. **Check Squarespace support:**
   - Squarespace DNS documentation
   - Contact Squarespace support for DNS questions

4. **GitHub Pages documentation:**
   https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site

---

## Post-Setup Checklist

Once everything works:

- [ ] Site loads at https://rodrigallardo.art
- [ ] HTTPS enabled (green padlock in browser)
- [ ] www subdomain redirects to apex domain
- [ ] All images load correctly
- [ ] Language switcher works (ES/EN)
- [ ] WhatsApp buttons work
- [ ] Google Analytics tracking works

---

**Last Updated:** 2026-02-13
