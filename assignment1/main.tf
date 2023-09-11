provider "aws" {
  region = "us-east-1" 
}

resource "aws_vpc" "my_vpc" {
  instance_type = "t2.micro"
  ami = ""
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
}

resource "aws_subnet" "public_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a" 
}

resource "aws_subnet" "private_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "us-east-1b" 
}

resource "aws_security_group" "my_security_group" {
  name_prefix = "my-security-group-"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  vpc_id = aws_vpc.my_vpc.id
}

resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0" 
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id
  associate_public_ip_address = true

  root_block_device {
    volume_size = 8
    volume_type = "gp2"
  }

  tags = {
    "Name"    = "MyInstance"
    "purpose" = "Assignment"
  }

  depends_on = [aws_security_group.my_security_group]
}
