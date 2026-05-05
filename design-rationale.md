ICTN 6875
Alister Edens

Introduction
Network automation has become a fundamental practice in modern IT environments, allowing administrators to manage increasingly complex infrastructures with greater speed and consistency. However, while automation improves efficiency, it also introduces significant risk when safeguards such as validation and rollback are not incorporated. A single bad configuration, when deployed automatically, can cause a cascade of issues and result in widespread outages or poor performance.
The lab addresses a critical gap in many automation workflows: the lack of integrated verification and recovery mechanisms. Traditional approaches often focus on executing configuration changes but fail to confirm whether those changes produce the intended outcome. Without validation, errors may go undetected. Without rollback, recovery may require time-consuming manual intervention, losing organizations precious resources.
This paper serves to justify the architectural and implementation decisions for a closed-loop automation framework, in which configuration changes are not only applied but also verified and reversed if necessary. The design focuses on a simplified environment consisting of an Ubuntu virtual machine acting as the automation controller and a Cisco CSR1000v router as the managed device. The lab emphasizes reliability, safety, and educational accessibility while exposing students to realistic automation challenges.

Problem Definition and Requirements
Manual network configuration is inherently error-prone due to human limitations, including inconsistent command entry and lack of repeatability. Automation addresses these issues but introduces a different class of risk: systematic failure at scale. If an automated script contains an error, it can replicate that error across multiple devices instantly.
A key weakness in many automation implementations is the absence of a closed-loop process. Changes are executed but not validated. Even when backups are taken, they are often disconnected from the execution workflow and not used for recovery. This creates a scenario where automation increases speed but not necessarily reliability, as it’s ignoring validation.
The lab’s automation approach must integrate pre-change backups, post-change validation, and automated recovery mechanisms in the event of something going wrong.

In other words, these are requirements necessary for this lab’s goal.
•	Establish an SSH connection to the network device
•	Perform a configuration backup prior to any changes
•	Apply a predefined configuration change
•	Validate the resulting device state
•	Implement rollback if validation fails
•	Provide observable outputs for educational purposes
The lab must be also accessible to undergraduate students with somewhat limited automation experience. For this reason, the implementation avoids unnecessary complexity but still demonstrates key concepts for robust automation.

Architecture and Design Outline
The system follows a simple two-node architecture:
•	DEVASC VM: Ubuntu host for the Python automation script
•	CSR1000v Router: Acts as the managed network device
 
Topology addresses will change from student to student.

As instructed, we will be using the provided DEVASC and CSR1000v virtual machines due to their simplicity and ease of deployment. While more complex architecture exists, they would introduce additional setup complexity that may distract from the core learning objectives here.
For the automation, Python was selected due to its readability, widespread industry adoption, and suitability for beginners. Its extensive libraries make it a practical choice for network automation solutions.

Netmiko was chosen to handle SSH communication. While alternatives such as Paramiko provide lower-level control, Netmiko is simple and easy to use for the scope of the lab.  By using it, students will focus on automation logic rather than connection management.
A key design tradeoff was the decision to use CLI-based automation instead of API-based approaches (e.g., RESTCONF or NETCONF). While APIs are more robust and structured, CLI automation remains widely used both in industry and the classroom. The tradeoff sacrifices some reliability and structure in favor of accessibility and realism.

Workflow Design (Closed-Loop Model)
This design reflects real-world best practices, where automation must include verification checkpoints along the way. The system follows a sequential workflow:
1.	Establish connection
2.	Perform configuration backup
3.	Apply configuration change
4.	Validate device state
5.	Rollback if validation fails

Failure Scenario Implementation 
Including a toggle for a failure scenario allows the system to simulate incorrect configurations, forcing validation to fail and triggering rollback. This was implemented to address a common limitation in our labs: we often only experience successful outcomes. By introducing controlled failure, the lab prepares students for real-world conditions where automation does not always behave as expected. 

Backup Strategy
The system captures the running configuration using a CLI command and stores it in a local file. This approach is simple and effective but introduces some tradeoffs. The backup method is easy to implement and does grab the full configuration of the device, but it may be tricky to do partial rollbacks for when only some commands were incorrect.

Validation 
Validation is performed using string matching against CLI output. This method is simple and accessible but has a few limitations:
•	It may produce false positives
•	It depends on consistent CLI output formatting
Despite these limitations, the approach is appropriate for this level of introductory lab. It introduces the concept of validation without requiring advanced tools. Future improvements could include structured parsing using libraries such as Genie.

Rollback Mechanism
Rollback is implemented by reapplying the previously saved configuration in backup.txt. This allows the device to return to a safe configuration state if needed. There are some issues in this approach as well:
•	The ordering of commands may affect results
•	Some configurations may not revert cleanly if other changes are made
•	Partial rollback scenarios are not handled
By exposing students to some of these limitations they will understand that rollback is not trivial and must be carefully designed in production systems.

Error Handling and Risk Mitigation
Basic error handling is implemented through conditional checks and controlled adding to the automation script. The current design has some room for error, but mostly boils down to improper commands or indentation. Risk mitigation is achieved through  backups to preserve system, validation checks to detect incorrect configurations (simulated with the FAIL_MODE variable), and rollback mechanisms for recovery. These factors reduce the likelihood of prolonged misconfiguration and align with best practices in reliable system network design.



Conclusion
This lab demonstrates a practical approach to building safe and reliable network automation systems. By integrating backup, validation, and rollback into a unified workflow, the implementation addresses a critical gap in traditional automation practices.
The chosen design balances simplicity and functionality, making it suitable for educational use while still reflecting real-world challenges in the field. Ultimately, this lab provides a foundation for more advanced automation systems and teaches students about the skills necessary to design and evaluate safe automation solutions in professional environments.









References
Nichols, L. (2023). Cybersecurity architect’s handbook. Wiley.
Byers, K. (2024). Netmiko documentation. GitHub. https://github.com/ktbyers/netmiko
Wilkins, S. (2021). Network automation with Python and Ansible. Packt Publishing.
