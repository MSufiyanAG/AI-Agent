# DEPLOY-AI-AGENT Backend — Setup & Deployment Guide

Follow these steps to deploy your backend using GitHub, Docker, and Railway, and make it live with a database and environment configuration.

---

1. **Fork the Repository**
   - Create a copy of this project in your own GitHub account to customize and deploy.

2. **Connect to Railway**
   - In [Railway](https://railway.app), create or select your project.
   - Link your GitHub repository to the Railway project as the deployment source.

3. **Add a PostgreSQL Database**
   - In your Railway project environment, add a PostgreSQL database plugin.

4. **Set Deployment Settings**
   - Go to your deployment in Railway and open the **Settings**.
   - Set the **root directory** to `DEPLOY-AI-AGENT/backend` (where your Dockerfile is located).

5. **Specify Railway Configuration**
   - Add the path to your Railway configuration file: `DEPLOY-AI-AGENT/backend/railway.json`.

6. **Configure Environment Variables**
   - In the **Variables** section:
     - Add `DATABASE_URL` using the connection string from the PostgreSQL database you just created.
     - Add `EMAIL_ADDRESS` and `EMAIL_PASSWORD` (use an app password for email).
     - Add `OPENAI_API_KEY` for OpenAI access.

7. **Deploy**
   - Deploy your backend by pushing any new changes. Railway will build and deploy your project.

8. **Assign a Public Domain**
   - Once deployment is complete, go to **Settings > Networking** in Railway.
   - Click **Generate Domain** and enter the backend port (For us: 8000).

9. **Verify the Deployment**
   - Your backend should now be live with a public URL.
   - Visiting the domain should display a hello message or indicate the backend is running. If a frontend is connected, you should see it communicating with the backend.
  
10. **Scheduled Backend API Access**
    - The backend API is being accessed automatically each day via a scheduled `curl` command, configured in your GitHub Actions workflow.  
    - This ensures your service regularly receives external requests and performs its automation as intended.

---

For any issues, check your deployment logs and verify environment variables and file paths. Happy coding! 🚀

https://github.com/user-attachments/assets/b772042a-764a-441b-af0d-86bdbdf8a5e9

![image.png](attachment:2045cf39-cdb6-4530-877c-7d2fa16810c8:image.png)

<img width="1082" height="798" alt="drawing_arch" src="https://github.com/user-attachments/assets/22c386d4-8133-495d-bff9-ceafe6dc396f" />
