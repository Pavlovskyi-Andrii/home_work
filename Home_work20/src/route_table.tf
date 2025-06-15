resource "aws_route_table" "andrey_route_table" {
  vpc_id = aws_vpc.andrey-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.andrey_gw.id
  }

  tags = {
    Name = "andrey_route_table"
  }
}

resource "aws_route_table_association" "andrey_route_table_association" {
  subnet_id      = aws_subnet.andrey_sybnet.id
  route_table_id = aws_route_table.andrey_route_table.id
}