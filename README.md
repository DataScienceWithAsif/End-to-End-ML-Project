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

**Special Thanks:** Huge thanks to [@krishnaik06](https://github.com/krishnaik06) for the guidance so far. If anyone (including the legend himself!) has encountered this specific pipeline error while following the modular deployment flow, I’d love to connect and resolve this.

## 🤝 Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is appreciated.

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide to learn how to contribute to this project and open source projects in general.

### Quick Start for Contributors
1. Fork the repository
2. Clone your fork
3. Create a new branch for your changes
4. Make your changes and test them
5. Submit a pull request

For detailed guidelines, please see [CONTRIBUTING.md](CONTRIBUTING.md).
