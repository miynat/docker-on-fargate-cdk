from aws_cdk import (
    core as cdk,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
)


class FactorialCalculatorStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "Service",
            memory_limit_mib=1024,
            cpu=512,
            desired_count=2,
            task_image_options={"image": ecs.ContainerImage.from_asset("docker/")},
        )
