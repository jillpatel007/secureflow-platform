terraform {
  required_providers {
    kind = {
      source  = "tehcyx/kind"
      version = "~> 0.9"
    }
  }
}

provider "kind" {}

resource "kind_cluster" "default" {
  name           = "devsecops"
  wait_for_ready = true
}
