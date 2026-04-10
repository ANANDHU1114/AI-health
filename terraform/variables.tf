variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
  default     = "ai-health-rg"
}

variable "location" {
  description = "Azure region for deployment"
  type        = string
  default     = "East US"
}

variable "acr_name" {
  description = "Name of the Azure Container Registry"
  type        = string
  default     = "aihealthacrdevops" # Must be globally unique and lowercase
}

variable "aks_cluster_name" {
  description = "Name of the Azure Kubernetes Service cluster"
  type        = string
  default     = "ai-health-aks"
}

variable "dns_prefix" {
  description = "DNS prefix for the AKS cluster"
  type        = string
  default     = "pulseai-aks"
}

variable "node_count" {
  description = "Number of nodes in the AKS cluster"
  type        = number
  default     = 2
}

variable "vm_size" {
  description = "Size of the VM nodes"
  type        = string
  default     = "Standard_B2s" # Cost effective for academic demo
}
