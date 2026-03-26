# KyberForge Project Governance

The development and community management of the KyberForge project will follow the governance rules described in this document.

## Project Maintainer

The project maintainer has admin access to the GitHub repository. The project maintainer is:

* [Aldo E Jimenez](https://github.com/tech-architecti/)

## 1. Roles

This project includes the following roles:

1.1. **Maintainer**. The maintainer is responsible for organizing activities around developing, maintaining, and updating the KyberForge project. The project maintainer will review and merge pull requests.

1.2. **Collaborator**. Any member willing to participate in the development of the project will be considered as a **collaborator**. Collaborators may propose changes to the project's source code. The mechanism to propose such a change is a GitHub pull request. A collaborator proposing a pull request is considered a **contributor**. 

## 2. Issue Governance

2.1. Both collaborators and the project maintainer may propose issues. The participation in the issue discussion is open and must follow the [Code of Conduct](CODE_OF_CONDUCT.md).

2.2. The project maintainer will be responsible for assigning labels to issues, as well as assigning the issue to themselves or a contributor.

2.3. The project maintainer commits to give an answer to any issue within 48 hours. 

## 3. Pull Request Governance

3.1. Both collaborators and the project maintainer may propose pull requests. When a collaborator proposes a pull request, they are considered a contributor.

3.2. Pull requests should comply with the template provided. The assignment of labels and assignees to the pull request is the responsibility of the project maintainer.

3.3. The project maintainer commits to give an answer to any pull request within 48 hours. 

3.4. The decision of accepting (or rejecting) a pull request will be taken by the project maintainer. The decision will be based on the following criteria:

* The project maintainer must approve a pull request before it can be merged. 
* If the pull request has been open for more than 14 days without any opposition, it can be merged with a single approval from the project maintainer.
* Approving a pull request indicates that the contributor accepts responsibility for the change. 
* If the project maintainer opposes a pull request, the pull request cannot be merged (i.e., _veto_ behavior). Often, discussions or further changes result in the maintainer removing their opposition.

## 4. Release Management

4.1. The project maintainer is responsible for managing the release process.

4.2. A new release should be published whenever significant changes or improvements have been made to the project.

4.3. Before a new release, the project maintainer should ensure that:
   - All tests are passing
   - The documentation is up to date
   - A changelog is prepared, outlining the changes in the new release
   - Version numbers follow [Semantic Versioning](https://semver.org/)
   - All dependencies are up to date
   - Security checks have passed

4.4. The project maintainer will create a new release on GitHub, which will automatically trigger the CI/CD pipeline to build and deploy the new version.

## 5. Version Control

5.1. The project follows the [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) branching strategy:

- `main` contains production-ready code
- `develop` contains integration/development code
- Feature branches are created from `develop` and merged back into `develop`
- Release branches are created from `develop`, then merged into `main` and back into `develop` when finished
- Hotfix branches are created from `main`, then merged into both `main` and `develop`

5.2. Branch naming convention:
   - Feature branches: `name/feature/description`
   - Bug fix branches: `name/fix/kyb1234-description`
   - Release branches: `release/version` i.e. `release/1.2.0`
   - Hotfix branches: `hotfix/kyb1234-description`

## 6. Changes to this Governance Document

6.1. Changes to this governance document can be proposed via a pull request.

6.2. The decision to accept changes to this document will be made by the project maintainer, following the same criteria as for regular pull requests.

6.3. If accepted, the changes will be incorporated into the governance document, and the updated version will be committed to the repository.

## 7. Contact

For any questions about this governance document or the project in general, please contact:

* Email: info@techarchitecti.com
* GitHub: [@tech-architecti](https://github.com/tech-architecti)
* Project Repository: https://github.com/tech-architecti/KyberForge
