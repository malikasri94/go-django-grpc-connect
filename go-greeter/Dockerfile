# go-greeter/Dockerfile

FROM golang:1.23 as builder

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o greeter .

CMD ["./greeter"]
