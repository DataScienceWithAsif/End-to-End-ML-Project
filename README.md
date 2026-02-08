# ***Student Performance Indicator***
<img width="1323" height="594" alt="image" src="https://github.com/user-attachments/assets/8f2c030a-1761-4b8c-8c1d-a669adb1b734" />

<img width="1359" height="695" alt="image" src="https://github.com/user-attachments/assets/ffbec8b3-6d08-40f8-a921-0966006180e0" />

## Deployment Journey

### AWS (Work in Progress)
I initially attempted to deploy this using **AWS CodePipeline** and **Elastic Beanstalk**. 
- **Status:** Resolved IAM policy permission issues. 
- **Current Blocker:** Encountering an **'Action execution failed'** during the build stage. I am currently debugging the buildspec.yml and environment configurations.

### Hugging Face (Live)
To ensure the application was accessible while AWS debugging continues, I containerized the application using **Docker** and deployed it to **Hugging Face Spaces**.
