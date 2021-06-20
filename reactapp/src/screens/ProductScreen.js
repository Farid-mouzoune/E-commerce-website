import React, {useState, useEffect} from 'react'
import { Link } from 'react-router-dom'
import { Row, Col, Image, Card, ListGroup, Button } from 'react-bootstrap'
import Rating from '../components/Rating'
import axios from 'axios'


function ProductScreen({ match }) {
    const [ product, setProduct ] = useState([])
    useEffect(() => {

        async function fetchProduct(){
            const { data } = await axios.get(`/api/products/${match.params.id}/`)
            setProduct(data)
        }
        fetchProduct()

    },[])
    return (
        <div>

            <Link to='/' className='btn btn-dark my-3'>Back</Link>
            <Row>

                <Col md={6}>
                    <Image src={product.image} alt={product.name} fluid/> 

                </Col>
                <Col md={3}>

                    <ListGroup variant="flash" className="text-center">
                        <ListGroup.Item>
                            <h3>{product.name}</h3>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'} />
                        </ListGroup.Item>
                        <ListGroup.Item>
                            Price : {product.price}$
                        </ListGroup.Item>
                        <ListGroup.Item>
                            Description : {product.description}
                        </ListGroup.Item>

                    </ListGroup>

                </Col>
                <Col md={3}>
                    <Card>
                    <ListGroup variant="flash" className="text-center">
                        <ListGroup.Item>
                            <Row>
                                <Col>Price :</Col>
                                <Col>{product.price} $</Col>
                            </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            <Row>
                                <Col>In Stock :</Col>
                                <Col>{product.countInStock > 0 ?'In Stock' : 'Out Of Sotck'}</Col>
                            </Row>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            <Row>
                                <Button className="btn-block" disabled={product.countInStock === 0} type="button">Add to Cart</Button>
                            </Row>
                        </ListGroup.Item>
                    </ListGroup>

                    </Card>
                </Col>

            </Row>


        </div>
    )
}

export default ProductScreen
