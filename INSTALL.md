# Kubeflow install in AWS


## Install kubeflow
<https://www.kubeflow.org/docs/distributions/aws/deploy/install-kubeflow/>

1. set ENV
```
export AWS_CLUSTER_NAME=kubeflow-demo-sheum
export AWS_REGION=ap-northeast-2
export K8S_VERSION=1.18
export EC2_INSTANCE_TYPE=m5.large
```

2. make Cluster
```
$ cat cluster.yaml
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig

metadata:
  name: kubeflow-demo-sheum
  version: "1.18"
  region: ap-northeast-2

managedNodeGroups:
- name: kubeflow-mng-sheum
  desiredCapacity: 3
  instanceType: m5.large
```

```
eksctl create cluster -f cluster.yaml
```

3. (if not exist) aws-iam-authenticator install
```
https://docs.aws.amazon.com/ko_kr/eks/latest/userguide/install-aws-iam-authenticator.html
```

4. kfctl apply
```
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.2-branch/kfdef/kfctl_aws.v1.2.0.yaml"

mkdir ${AWS_CLUSTER_NAME} && cd ${AWS_CLUSTER_NAME}

wget -O kfctl_aws.yaml $CONFIG_URI
kfctl apply -V -f kfctl_aws.yaml
```

5. check status
```
kubectl -n kubeflow get all
kubectl get ingress -n istio-system
```

-----------
## Uninstall

```
kfctl delete -V -f kfctl_aws.yaml

eksctl delete cluster -f cluster.yaml
```
